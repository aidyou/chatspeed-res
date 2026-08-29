import { hasGlobalComponent } from "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.130_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13.3_@v_4c97be4a6a919dc4469960b09c1ca2e7/node_modules/@vuepress/helper/dist/client/index.js";
import Badge from "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/vuepress-plugin-components@2.0.0-rc.107_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@_d1d85958b7f991dbe408246d27a8704f/node_modules/vuepress-plugin-components/dist/client/components/Badge.js";

import "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.130_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13.3_@v_4c97be4a6a919dc4469960b09c1ca2e7/node_modules/@vuepress/helper/dist/client/styles/sr-only.css";

export default {
  enhance: ({ app }) => {
    if(!hasGlobalComponent("Badge")) app.component("Badge", Badge);
    
  },
  setup: () => {

  },
  rootComponents: [

  ],
};
