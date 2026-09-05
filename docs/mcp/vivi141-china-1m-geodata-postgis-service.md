---
title: "China_1M_GeoData_PostGIS_MCP_Service"
description: "A PostGIS MCP service specially designed for the 1:1,000,000 basic geographic information data of the National Catalogue Service For Geographic Information, allowing AI assistants to directly access a…"
---

# China_1M_GeoData_PostGIS_MCP_Service

A PostGIS MCP service specially designed for the 1:1,000,000 basic geographic information data of the National Catalogue Service For Geographic Information, allowing AI assistants to directly access a…

# 1:1,000,000 Basic Geographic Information PostGIS MCP Service

**China 1M GeoData PostGIS MCP Service**

[![Python](/mcp-assets/d59218ebaf72462fc74fe3c1ee52295b.svg)](https://www.python.org/)
[![PostgreSQL](/mcp-assets/7915dee1fb10ec76ecf647b4091451c1.svg)](https://www.postgresql.org/)
[![PostGIS](/mcp-assets/2e99a3d9cccc8942a8d0df2ab99e81ad.svg)](https://postgis.net/)
[![MCP](/mcp-assets/799859e8ca2cf5a585b9c0afcea682c5.svg)](https://modelcontextprotocol.io/)
![License](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)

A PostGIS MCP service specially designed for the 1:1,000,000 basic geographic information data of the National Catalogue Service For Geographic Information, allowing AI assistants to directly access and query spatial geographic data in PostgreSQL/PostGIS through the Model Context Protocol (MCP).

## Project Introduction

This project is an **enterprise-grade PostGIS spatial data MCP service**, focused on importing the 1:1,000,000 public-version basic geographic information data (2021) into PostgreSQL/PostGIS, and providing powerful spatial query, analysis, and interaction capabilities through the MCP protocol. The project supports one-click Docker deployment and provides a complete toolchain, making geographic data queries simple and efficient.

### Core Features

- **MCP protocol integration**: compliant with the Model Context Protocol standard, seamlessly integrable with AI assistants such as Claude and GPT
- **Unified table structure**: intelligently designed unified table structure supporting unified management and querying of multi-sheet data
- **High-performance querying**: based on PostgreSQL/PostGIS spatial indexes (GIST), enabling millisecond-level spatial queries
- **One-click deployment**: supports Docker Compose one-click deployment, including PostgreSQL, the MCP service, and the Supergateway gateway
- **Complete toolchain**: provides a full toolset from data parsing, table structure design, data import to verification
- **Data quality assurance**: automatically validates and repairs invalid geometries to ensure data integrity
- **Detailed documentation**: a complete documentation system including field descriptions, table usage guides, query examples, etc.
- **Remote access**: supports the Supergateway gateway for HTTP/SSE/WebSocket remote access

### Differences from PostgreMCP

**PostgreMCP** focuses on database management and optimization (analysis, debugging, configuration), while **our service** focuses on PostGIS spatial data operations:

| Feature | PostgreMCP | Our Service |
|------|-----------|-----------|
| Database management | Yes: analysis, optimization, debugging | No |
| PostGIS spatial queries | No | Yes: spatial query, spatial analysis |
| Geographic data import | No | Yes: GDB import to PostGIS (provides data for the service) |
| SQL queries | No | Yes: supports PostGIS spatial SQL queries |
| PostGIS support | No | Yes: dedicated PostGIS support |

**The two services complement each other**: use our service for PostGIS spatial data query and analysis, and PostgreMCP for database performance optimization.

### Use Cases

- **AI assistant integration**: let AI assistants such as Claude and GPT understand and query Chinese geographic data
- **Geographic information queries**: quickly query geographic features such as administrative divisions, water systems, and transportation
- **Spatial analysis**: perform complex spatial analysis such as buffer analysis, spatial intersection, and distance calculation
- **Geographic location lookup**: query surrounding geographic features by longitude/latitude, or find coordinates by place name
- **Data visualization**: provide backend data support for GIS applications and map services
- **Government applications**: support geographic data query and analysis needs in government systems

### Core Capabilities

- **Spatial data query**: supports spatial filtering, attribute filtering, and complex spatial analysis queries
- **PostGIS SQL execution**: supports all PostGIS spatial functions (ST_Area, ST_Distance, ST_Buffer, etc.)
- **GDB data import**: supports batch import of GDB-format geographic databases with automatic tile code recognition
- **Unified table structure**: intelligently parses and creates a unified table structure; multi-sheet data shares the table design
- **Data verification**: automatically validates geometry validity, repairs invalid geometries, and reports import results
- **Tile management**: automatically recognizes and manages standard 1:1,000,000 tile codes (F49, G50, etc.)
- **Field documentation**: automatically generates field description documents to help understand the data

### Production Status

**Successfully deployed in production**

This project has been successfully deployed and is running stably on a **cloud Linux server**, and has successfully connected with LLMs (large language models), verifying the following capabilities:

- **Cloud deployment**: successfully deployed in a Linux production environment
- **LLM integration**: successfully established MCP connections with AI assistants (Claude, GPT, etc.)
- **Data querying**: spatial data query and analysis functions work normally
- **Stable performance**: runs stably in production with timely query responses

**Deployment environment**:
- OS: Linux (cloud server)
- Deployment method: Docker Compose
- Database: PostgreSQL/PostGIS
- Gateway: Supergateway (supports remote access)
- Status: running in production

**Applicable scenarios**:
- **Production**: successfully deployed on a cloud Linux server
- **Development**: supports local Windows/Linux development
- **Hybrid deployment**: supports separate development and production environments

### Data Source and Customization

This project is custom-developed for the 1:1,000,000 public-version basic geographic information data (2021) of the National Catalogue Service For Geographic Information. It has been deeply optimized and verified in production, and can be used directly in production environments.

#### Data Overview

**1:1,000,000 public-version basic geographic information data (2021)**
- **Coverage**: all national land and major islands (Taiwan Island, Hainan Island, Diaoyu Island, South China Sea Islands, etc.)
- **Number of sheets**: 77 standard 1:1,000,000 sheets
- **Data currency**: 2019
- **Coordinate system**: China Geodetic Coordinate System 2000 (CGCS2000), 1985 National Height Datum, longitude/latitude coordinates (SRID: 4326)
- **Data source**: authorized by the Ministry of Natural Resources, provided free of charge by the National Catalogue Service For Geographic Information

**9 major geographic feature datasets**:
1. **Water systems**: rivers, lakes, reservoirs, and other water features
2. **Settlements and facilities**: cities, towns, villages, and other residential areas
3. **Transportation**: highways, railways, airports, and other transport facilities
4. **Pipelines**: oil pipelines, power lines, and other pipeline features
5. **Boundaries and administrative regions**: provincial, municipal, and county administrative boundaries
6. **Landforms and soils**: terrain and geological features
7. **Vegetation**: forests, grasslands, and other vegetation cover
8. **Place names and annotations**: place names and geographic annotation information
9. **Positioning foundation**: survey control points and coordinate grids

#### Project Advantages

- **Ready to use out of the box**: built-in complete data specification configuration (`china_1m_2021`), no manual configuration needed
- **Intelligent recognition**: automatically recognizes tile codes (F49, G50, etc.) and extracts tile information
- **Unified management**: unified table structure design, seamless integration of multi-sheet data
- **Complete toolchain**: full automated workflow from data parsing to import verification
- **Field documentation**: automatically generates field description documents, lowering the usage barrier

### Technical Architecture

```
+---------------------------------------------------------+
|                  AI Assistant (Claude/GPT)               |
|                  communicates via MCP protocol           |
+---------------------------+-----------------------------+
                            |
                            v
+---------------------------------------------------------+
|            MCP Server (mcp_server.py)                    |
|  - list_tile_codes  - list_tables  - verify_import      |
|  - query_data  - execute_sql                            |
+---------------------------+-----------------------------+
                            |
                            v
+---------------------------------------------------------+
|          PostgreSQL/PostGIS Database                     |
|  - spatial indexes (GIST) - spatial data types - PostGIS |
|  - unified table structure - multi-sheet data integration|
+---------------------------+-----------------------------+
                            |
                            v
+---------------------------------------------------------+
|              Data Import Toolchain                       |
|  - parse_tile_schema  - create_unified_schema           |
|  - import_all_tiles  - verify_data                      |
+---------------------------+-----------------------------+
                            |
                            v
+---------------------------------------------------------+
|            GDB Geographic Database Files (1:1M)          |
|  F49.gdb  F50.gdb  G49.gdb  G50.gdb ... (77 sheets)     |
+---------------------------------------------------------+
```

**Deployment methods**:
- **Pure Windows & Linux deployment**: install dependencies and run directly on Windows or Linux, suitable for development and testing environments
- **Windows & Linux + Docker deployment** (recommended): one-click deployment with Docker Compose, supports local and remote access, suitable for production environments
  - **Verified**: successfully deployed and stably running on a cloud Linux server
  - **LLM integration**: successfully established MCP connections with AI assistants and communicating normally

## Quick Start

Choose a deployment method based on your needs:

### Method 1: Pure Windows & Linux deployment

#### System requirements

- **Windows 10/11** or **Linux** (Ubuntu 20.04+, Debian 11+, CentOS 8+, etc.)
- **Python 3.8+**
- **PostgreSQL 9.5+** (PostgreSQL 12+ recommended) - **required**
- **PostGIS 2.5+** extension - **required**
- **GDAL/OGR libraries** (for reading GDB files)

#### 1. Install dependencies

**Windows (conda recommended)**
```powershell
conda install -c conda-forge gdal fiona shapely psycopg2
pip install -r requirements.txt
```

**Linux**
```bash
# Ubuntu/Debian
sudo apt-get install gdal-bin libgdal-dev python3-gdal

# CentOS/RHEL
sudo yum install gdal gdal-devel python3-gdal

# Or use conda
conda install -c conda-forge gdal fiona shapely psycopg2

pip install -r requirements.txt
```

#### 2. Install and configure PostgreSQL/PostGIS

**Windows:**
1. Download and install [PostgreSQL](https://www.postgresql.org/download/windows/)
2. Select the PostGIS extension during installation
3. Or install the PostGIS extension with a package manager

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib postgis

# CentOS/RHEL
sudo yum install postgresql postgresql-server postgis
```

**Create the database and enable PostGIS:**
```sql
CREATE DATABASE gis_data;
\c gis_data
CREATE EXTENSION postgis;
```

#### 3. Configure connection info

```bash
# Copy the configuration template
cp config/database.ini.example config/database.ini

# Edit the config file and fill in the database connection info
# Windows: notepad config/database.ini
# Linux: nano config/database.ini
```

#### 4. Run the MCP server

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
python mcp_server.py

# Linux
source .venv/bin/activate
python mcp_server.py
```

#### 5. Configure in the MCP client

**Basic configuration example (using absolute paths):**

```json
{
  "mcpServers": {
    "china-1m-geodata-postgis-mcp": {
      "command": "python",
      "args": [
        "C:/Users/YourUsername/Desktop/gdb_mcp/mcp_server.py"
      ],
      "cwd": "C:/Users/YourUsername/Desktop/gdb_mcp"
    }
  }
}
```

**Using a virtual environment (recommended):**

```json
{
  "mcpServers": {
    "china-1m-geodata-postgis-mcp": {
      "command": "C:/Users/YourUsername/Desktop/gdb_mcp/.venv/Scripts/python.exe",
      "args": [
        "C:/Users/YourUsername/Desktop/gdb_mcp/mcp_server.py"
      ],
      "cwd": "C:/Users/YourUsername/Desktop/gdb_mcp"
    }
  }
}
```

**Notes:**
- Must use **absolute paths**
- Setting `cwd` to the project root is recommended
- Using a virtual environment is recommended
- See the [complete MCP service guide](https://github.com/ViVi141/china-1m-geodata-postgis-mcp/blob/HEAD/docs/MCP_GUIDE.md) for detailed configuration

---

### Method 2: Windows & Linux + Docker deployment (recommended)

#### System requirements

- **Windows 10/11** (WSL2 required) or **Linux** (Ubuntu 20.04+, Debian 11+, CentOS 8+, etc.)
- **Docker 20.10+**
- **Docker Compose 2.0+** (or use the `docker compose` command)

#### Quick deployment

**1. Create the environment variable file**

Create a `.env` file in the project root:

```bash
POSTGRES_DB=gis_data
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password
POSTGRES_PORT=5432
GATEWAY_SSE_PORT=8000
GATEWAY_WS_PORT=8001
GATEWAY_LOG_LEVEL=info
```

**2. Start the service**

```bash
# Start the basic services (PostgreSQL + MCP server)
docker-compose up -d

# Start the full services (including Supergateway, supports remote access)
docker-compose --profile gateway up -d

# Or use the standalone script to start Supergateway (recommended)
# Linux: ./scripts/start-supergateway.sh
# Windows: .\scripts\start-supergateway.bat
```

**3. Verify the service**

```bash
# Check the service status
docker-compose ps

# Check PostgreSQL
docker-compose exec postgres psql -U postgres -d gis_data -c "SELECT PostGIS_Version();"

# Check Supergateway (if enabled)
# Supergateway does not provide a /health endpoint by default; use /sse to verify
curl -i --max-time 2 http://localhost:8000/sse
```

**4. Configure in the MCP client**

**Docker deployment configuration (recommended):**

```json
{
  "mcpServers": {
    "china-1m-geodata-postgis-mcp": {
      "command": "docker",
      "args": [
        "exec",
        "-i",
        "geodata-mcp-server",
        "python",
        "/app/mcp_server.py"
      ]
    }
  }
}
```

**Common commands:**

```bash
# Stop the service
docker-compose stop

# Stop and remove containers
docker-compose down

# View logs
docker-compose logs -f

# Enter a container
docker-compose exec mcp-server bash
docker-compose exec postgres psql -U postgres -d gis_data
```

**Detailed deployment docs:**
- **Complete Docker deployment guide**: see [Docker deployment guide](https://github.com/ViVi141/china-1m-geodata-postgis-mcp/blob/HEAD/docs/DOCKER_GUIDE.md)
- **MCP client configuration**: see [MCP configuration guide](https://github.com/ViVi141/china-1m-geodata-postgis-mcp/blob/HEAD/docs/MCP_SERVER_CONFIG.md)

## Data Specification Configuration

### Default specification

The project includes the complete specification configuration for the **1:1,000,000 public-version basic geographic information data (2021)** (`specs/china_1m_2021.json`), containing layer mapping configurations for all 9 datasets.

### Creating a custom specification

Create a specification config file in JSON or YAML format:

```json
{
  "name": "my_custom_spec",
  "description": "Custom data specification",
  "version": "1.0.0",
  "default_srid": 4326,
  "tile_code_pattern": "auto",
  "layer_mapping": {
    "LAYER1": {
      "table_name": "custom_table_1",
      "description": "Layer 1 description",
      "category": "Category 1"
    }
  }
}
```

Save it to the `specs/` directory and it can be used in the MCP service.

## MCP Tools

**Note: the MCP service focuses on data query and analysis; it does not provide data import. Data import should be done with scripts.**

**Recommended workflow (unified table structure):**

**Method 1: use the unified toolset (easiest)**
```bash
python scripts/setup_unified_database.py
```

**Method 2: step by step**
1. Use `scripts/parse_tile_schema.py` to parse the tile structure
2. Use `scripts/create_unified_schema.py` to create the unified table structure
3. Use `scripts/import_all_tiles.py` to import all tile data

See the [unified table structure import guide](https://github.com/ViVi141/china-1m-geodata-postgis-mcp/blob/HEAD/docs/UNIFIED_SCHEMA_GUIDE.md) for details.

**Important notes:**
1. **Before querying, you must first use `list_tile_codes` to see which tiles are available**, then determine the tile to query based on the geographic location of the destination. Do not only query the F49 tile! See the [tile code guide](https://github.com/ViVi141/china-1m-geodata-postgis-mcp/blob/HEAD/docs/TILE_CODE_GUIDE.md) for details.
2. **Before querying, you must use `verify_import` to view the field descriptions** and understand the meaning of each field; do not guess field meanings. See the [field specification doc](https://github.com/ViVi141/china-1m-geodata-postgis-mcp/blob/HEAD/docs/FIELD_SPEC.md) for details.

### 1. list_tile_codes

Lists all imported tile codes in the database. **This is the first step before querying data and must be executed first!** Tile codes are globally standard 1:1,000,000 tile codes (such as F49, F50, G49, G50, etc.); each tile covers about a 6 degrees x 4 degrees geographic range. Determine the tile to query based on the geographic location of the destination. For example, Huizhou city is mainly in tiles F49 and F50, and Guangzhou city is mainly in tile F49.

**Parameters:**
- `database_config` (optional): database connection config

**Returns:** a list of tile codes, including record counts per table for each tile

### 2. list_tables

Lists all imported geographic data tables in the PostgreSQL/PostGIS database. Returns each table's name, record count, coordinate system (SRID), etc. **Before querying data, use this tool to see the available tables; do not blindly guess table names.**

**Parameters:**
- `database_config` (optional): database connection config

**Returns:** a table list, including table names, record counts, coordinate systems, etc.

### 3. verify_import

Verifies the imported data in PostgreSQL/PostGIS, checking data integrity, coordinate systems, geometry validity, spatial extents, etc. Returns each table's record count, SRID, bounding box (bbox), number of invalid geometries, and field info (including field descriptions). **This is an important tool for understanding table structures and field meanings; use it to view field descriptions before querying data, and do not guess field meanings.** See the [field specification doc](https://github.com/ViVi141/china-1m-geodata-postgis-mcp/blob/HEAD/docs/FIELD_SPEC.md) for details.

**Parameters:**
- `table_name` (optional): the table to verify (recommended to use list_tables first to see available tables); if not provided, verifies all tables
- `database_config` (optional): database connection config

### 4. query_data

Queries spatial data in PostgreSQL/PostGIS, supporting spatial and attribute filtering. **Suitable for simple spatial queries, such as queries by bounding box, by geometry intersection, by attribute filter, etc. For complex spatial analysis (such as calculating area, distance, buffers, spatial joins, etc.), use the execute_sql tool with PostGIS functions.**

**Parameters:**
- `table_name` (required): table name (must use list_tables first to see available tables)
- `spatial_filter` (optional): spatial filter conditions
  - `bbox`: bounding box [minx, miny, maxx, maxy], in degrees (longitude/latitude)
  - `geometry`: a WKT geometry, e.g. 'POINT(113.3 23.1)' or 'POLYGON((...))'
- `attribute_filter` (optional): attribute filter conditions as key-value pairs, e.g. {"tile_code": "F49"}
- `limit` (optional): result record limit (default 100)
- `database_config` (optional): database connection config

### 5. execute_sql

Executes SQL queries in the PostgreSQL/PostGIS database. **This is the main tool for complex spatial analysis and calculation.** Supports all PostGIS spatial functions, such as ST_Area (area), ST_Distance (distance), ST_Buffer (buffer), ST_Intersects (intersection test), ST_Within (containment test), ST_Union (merge), ST_Intersection (intersection), ST_Centroid (centroid), ST_Envelope (bounding box), etc.

**Applicable scenarios:**
- Spatial analysis (area, distance, buffer, spatial relationship tests)
- Spatial computation (merge, intersection, simplification, coordinate transformation)
- Complex queries (multi-table joins, aggregate statistics, spatial grouping)
- Data statistics (by region, by tile, etc.)

**Parameters:**
- `sql` (required): the SQL SELECT statement to execute. PostGIS spatial functions can be used, for example:
  - Area: `ST_Area(geom::geography)/1000000` (converts to square kilometers)
  - Distance: `ST_Distance(geom1::geography, geom2::geography)/1000` (converts to kilometers)
  - Spatial filter: `ST_Intersects(geom1, geom2)` or `geom && ST_MakeEnvelope(...)`
- `database_config` (optional): database connection config

**Note:** for security reasons, only SELECT query statements are allowed. See the [complete MCP service guide](https://github.com/ViVi141/china-1m-geodata-postgis-mcp/blob/HEAD/docs/MCP_GUIDE.md) for detailed usage and PostGIS function references.

## Project Structure

```
.
├── mcp_server.py              # Main MCP server file
├── core/                      # Core modules
│   ├── __init__.py
│   ├── config_manager.py      # Configuration management
│   ├── spec_loader.py         # Specification loader
│   ├── data_importer.py       # Data importer (optimized: connection pool, cache, performance monitoring)
│   ├── gdb_importer.py        # GDB importer
│   ├── logging_config.py      # Unified logging configuration
│   ├── connection_pool.py     # Connection pool management
│   ├── table_validator.py     # Table name validation (SQL injection protection)
│   ├── cache_manager.py       # Cache management (memory/Redis)
│   └── performance_monitor.py # Performance monitoring
├── specs/                     # Data specification configs
│   └── china_1m_2021.json     # 1:1,000,000 data specification
├── config/                    # Configuration files
│   ├── database.ini.example  # Database config template
│   └── database.ini          # Database config (not committed)
├── scripts/                   # Utility scripts (see scripts/README.md)
│   ├── setup_unified_database.py  # Unified toolset (strongly recommended)
│   ├── parse_tile_schema.py   # Fully parse the tile structure
│   ├── create_unified_schema.py  # Create the unified table structure
│   ├── import_all_tiles.py    # Import all tile data
│   ├── check.py               # Unified check tool (connection/layers/geometry quality)
│   ├── generate_field_spec.py # Generate field specification docs
│   ├── verify_data.py         # Verify imported data
│   ├── reset_database.py      # Reset the database
│   ├── start_mcp.bat/sh       # Start MCP (Windows/Linux)
│   └── start-supergateway.bat/sh  # Start Supergateway (Windows/Linux)
├── tests/                     # Unit tests
│   ├── __init__.py
```

(Remaining content, including detailed docs links, test configs, and license, follows the repository's docs/ directory.)

**Official site: ** [https://github.com/ViVi141/china-1m-geodata-postgis-mcp](https://github.com/ViVi141/china-1m-geodata-postgis-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `C:/Users/YourUsername/Desktop/gdb_mcp/mcp_server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/vivi141-china-1m-geodata-postgis-service.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
