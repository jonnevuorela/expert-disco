import adapter from "@sveltejs/adapter-static";
//export default config;
export default {
  kit: {
    adapter: adapter({
      fallback: "index.html", // may differ from host to host
    }),
  },
};
