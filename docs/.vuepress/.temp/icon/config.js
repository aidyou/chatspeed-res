import { hasGlobalComponent } from "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.130_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13.3_@v_4c97be4a6a919dc4469960b09c1ca2e7/node_modules/@vuepress/helper/dist/client/index.js";
import { useScriptTag } from "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vueuse+core@14.4.0_vue@3.5.42_typescript@5.9.3_/node_modules/@vueuse/core/dist/index.js";
import { h } from "vue";
import { VPIcon } from "/home/xc/dev/rust/chatspeed/chatspeed-res/node_modules/.pnpm/@vuepress+plugin-icon@2.0.0-rc.130_@vuepress+bundler-vite@2.0.0-rc.31_@types+node@24.13_f1837eedff6b714cd857acf0a3e22360/node_modules/@vuepress/plugin-icon/dist/client/index.js"

export default {
  enhance: ({ app }) => {
    if(!hasGlobalComponent("VPIcon")) {
      app.component(
        "VPIcon",
        (props) =>
          h(VPIcon, {
            type: "iconify",
            prefix: "",
            ...props,
          })
      )
    }
  },
  setup: () => {
    useScriptTag(`https://cdn.jsdelivr.net/npm/iconify-icon@2`);
  },
}
