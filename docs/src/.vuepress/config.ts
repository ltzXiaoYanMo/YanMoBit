import {defineUserConfig} from "vuepress";
import theme from "./theme.js";

export default defineUserConfig({
    base: "/",

    locales: {
        "/": {
            lang: "zh-CN",
            title: "YanMoBit",
            description: "YanMoBit 的使用、构建、开发文档",
        },
    },

    theme,
    shouldPrefetch: false,
});
