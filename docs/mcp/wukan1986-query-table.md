---
title: "query_table"
description: "A web scraper for financial table data that implements the Model Context Protocol, allowing users to query stock data from multiple Chinese financial websites including THS, TDX, and EastMoney."
---

# query_table

A web scraper for financial table data that implements the Model Context Protocol, allowing users to query stock data from multiple Chinese financial websites including THS, TDX, and EastMoney.

# mcp_query_table

1. A financial webpage table scraper built on `playwright`, supporting the `Model Context Protocol (MCP)`. Currently supported sources:

    - [THS iWencai](http://iwencai.com/)
    - [TDX Wenda](https://wenda.tdx.com.cn/)
    - [EastMoney Condition Stock Picker](https://xuangu.eastmoney.com/)

    In live trading, if one site goes down or is redesigned, you can switch to another site immediately. (Note: different sites have different table structures, so adaptation is needed in advance.)

2. An LLM-calling scraper built on `playwright`. Currently supported sources:
    - [Nano Search](https://www.n.cn/)
    - [Tencent Yuanbao](https://yuanbao.tencent.com/)
    - [Baidu AI Search](https://chat.baidu.com/)

    `RooCode` provides a `Human Reply` feature, but we found that copying from the `Nano Search` web version breaks the format, so this feature was developed.

## Installation

```commandline
pip install -i https://pypi.org/simple --upgrade mcp_query_table
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade mcp_query_table
```

## Usage

```python
import asyncio

from mcp_query_table import *

async def main() -> None:
    async with BrowserManager(cdp_endpoint="http://127.0.0.1:9222", executable_path=None, debug=True) as bm:
        # iWencai requires a browser width > 768 to prevent the mobile-adapted layout
        page = await bm.get_page()
        df = await query(page, 'the 200 ETFs with the best returns', query_type=QueryType.ETF, max_page=1, site=Site.THS)
        print(df.to_markdown())
        df = await query(page, 'top 50 by YTD return', query_type=QueryType.Fund, max_page=1, site=Site.TDX)
        print(df.to_csv())
        df = await query(page, 'top 10 industry sectors by float market cap', query_type=QueryType.Index, max_page=1, site=Site.TDX)
        print(df.to_csv())
        # TODO: EastMoney pagination requires logging in first
        df = await query(page, 'top 5 concept boards by today gain;', query_type=QueryType.Board, max_page=3, site=Site.EastMoney)
        print(df)

        output = await chat(page, "What is 1+2?", provider=Provider.YuanBao)
        print(output)
        output = await chat(page, "What is 3+4?", provider=Provider.YuanBao, create=True)
        print(output)

        print('done')
        bm.release_page(page)
        await page.wait_for_timeout(2000)

if __name__ == '__main__':
    asyncio.run(main())
```

## Notes

1. `Chrome` is preferred. If you must use `Edge`, besides closing all Edge windows, you also need to kill all `Microsoft Edge` processes in Task Manager, i.e. `taskkill /f /im msedge.exe`
2. Keep the browser window wide enough to prevent some sites from adapting to a mobile layout, which would break table queries
3. If you have an account on a site, log in in advance. This tool has no auto-login feature
4. Different sites have different table structures and return different numbers of stocks for the same condition. Adapt after querying

## How It Works

Unlike `requests`, `playwright` is browser-based and simulates user actions in the browser.

1. No need to solve login problems
2. No need to handle request construction and response parsing
3. Can grab table data directly - WYSIWYG
4. Slower than `requests`, but much more efficient to develop

Data can be obtained by:

1. Parsing HTML tables directly
    1. Numbers are textified, which is less convenient for later research
    2. Most universally applicable
2. Intercepting requests and grabbing the returned `json` data
    1. Similar to `requests`, requires response parsing
    2. Less flexible; after a site redesign, adaptation is needed again

This project sends requests by simulating browser clicks and obtains data by intercepting and parsing responses.

Later, we will switch to whichever method fits better as sites change.

## MCP Support

Make sure `python -m mcp_query_table -h` works in the console. If not, you may need to `pip install mcp_query_table` first.

You can configure it in `Cline` as follows. `command` is the absolute path to `python`, `executable_path` is the absolute path to `Chrome`, and `timeout` is the timeout in seconds.
On AI platforms, responses often take more than a minute, so set a large timeout.

### STDIO mode

```json
{
  "mcpServers": {
    "mcp_query_table": {
      "timeout": 300,
      "command": "D:\\Users\\Kan\\miniconda3\\envs\\py312\\python.exe",
      "args": [
        "-m",
        "mcp_query_table",
        "--format",
        "markdown",
        "--cdp_endpoint",
        "http://127.0.0.1:9222",
        "--executable_path",
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
      ]
    }
  }
}
```

### SSE mode

First start the `MCP` service from the console:

```commandline
python -m mcp_query_table --format markdown --transport sse --port 8000
```

Then connect to the `MCP` service:

```json
{
  "mcpServers": {
    "mcp_query_table": {
      "timeout": 300,
      "url": "http://127.0.0.1:8000/sse"
    }
  }
}
```

## Debugging with `MCP Inspector`

```commandline
npx @modelcontextprotocol/inspector python -m mcp_query_table --format markdown
```

Opening the browser and paging is time-consuming and can cause the `MCP Inspector` page to time out. Use `http://localhost:5173/?timeout=300000` to set the timeout to 300 seconds.

This is my first attempt at writing an `MCP` project, so there may be various issues - feedback is welcome.

## `MCP` Usage Tips

1. Top 100 stocks by 2024 gain ranked by total market cap on 2024-12-31. The three sites give different results:
    - THS: showed 2201 stocks. Top 5 were ICBC, Agricultural Bank of China, China Mobile, PetroChina, and China Construction Bank
    - TDX: showed 100 stocks. Top 5 were Cambricon, Zhengdan Co., Huijin Technology, Wanfeng Aowei, and Airong Software
    - EastMoney: showed 100 stocks. Top 5 were Hygon Information, Cambricon, Guangqi Technology, Runze Technology, and Xinyisheng

2. LLMs are weak at splitting questions, so ask carefully to make sure the query conditions are not altered. The 2nd and 3rd forms below are recommended:
    - Top 100 stocks by 2024 gain ranked by total market cap on 2024-12-31
      > The LLM will very likely split this sentence, turning one query into multiple queries
    - Ask EastMoney: "top 100 stocks by 2024 gain ranked by total market cap on 2024-12-31"
      > Put it in quotes to avoid being split
    - Ask the EastMoney sector: "the worst-performing industry sectors last year", then query the 5 best-performing stocks in that sector
      > Split into two steps: query the sector first, then the stocks. But full automation is not recommended, because the first step's result doesn't let the model understand the difference between "today's gain" and "period gain" - interactive correction is needed

## References

- [Playwright](https://playwright.dev/python/docs/intro)
- [Selenium webdriver cannot attach to edge instance, edge's --remote-debugging-port option is invalid](https://blog.csdn.net/qq_30576521/article/details/142370538)

**Official site: ** [https://github.com/wukan1986/query_table](https://github.com/wukan1986/query_table)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `browser`, `finance`
- Tags: `finance`, `browser automation`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `D:\Users\Kan\miniconda3\envs\py312\python.exe`
- Args: `-m mcp_query_table --format markdown --endpoint http://127.0.0.1:9222 --executable_path C:\Program Files\Google\Chrome\Application\chrome.exe`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wukan1986-query-table.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
