import { Layout, NotFound, injectDarkMode, setupDarkMode, setupSidebarItems, scrollPromise } from "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/vuepress-theme-hope@2.0.0-rc.107_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13.3_227ed6fc1161cbf465fdbe394e574315/node_modules/vuepress-theme-hope/dist/bundle/exports/base.js";

import { defineCatalogInfoGetter } from "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vuepress+plugin-catalog@2.0.0-rc.130_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24_f61b5f25cfa319eeaa52c2e409492868/node_modules/@vuepress/plugin-catalog/dist/client/index.js"
import { h } from "vue"
import { resolveComponent } from "vue"

import "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.130_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13.3_@v_4c97be4a6a919dc4469960b09c1ca2e7/node_modules/@vuepress/helper/dist/client/styles/colors.css";
import "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.130_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13.3_@v_4c97be4a6a919dc4469960b09c1ca2e7/node_modules/@vuepress/helper/dist/client/styles/normalize.css";
import "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.130_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13.3_@v_4c97be4a6a919dc4469960b09c1ca2e7/node_modules/@vuepress/helper/dist/client/styles/sr-only.css";
import "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/vuepress-theme-hope@2.0.0-rc.107_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13.3_227ed6fc1161cbf465fdbe394e574315/node_modules/vuepress-theme-hope/dist/client/styles/index.scss";

defineCatalogInfoGetter((meta) => {
  const title = meta.title;
  const shouldIndex = meta.index ?? true;
  const icon = meta.icon;

  return shouldIndex ? {
    title,
    content: icon ? () =>[h(resolveComponent("VPIcon"), { icon, sizing: "both" }), title] : null,
    order: meta.order,
    index: meta.index,
  } : null;
});

export default {
  enhance: ({ app, router }) => {
    const { scrollBehavior } = router.options;

    router.options.scrollBehavior = async (...args) => {
      await scrollPromise.wait();

      return scrollBehavior(...args);
    };

    // inject global properties
    injectDarkMode(app);


  },
  setup: () => {
    setupDarkMode();
    setupSidebarItems();

  },
  layouts: {
    Layout,
    NotFound,

  }
};
