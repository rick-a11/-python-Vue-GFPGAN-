"use strict";Object.defineProperty(exports, "__esModule", {value: true});

var _chunkBRLMGO66cjs = require('./chunk-BRLMGO66.cjs');
require('./chunk-K625S6OX.cjs');

// src/astro.ts
function astro_default(options) {
  return {
    name: "unplugin-auto-import",
    hooks: {
      "astro:config:setup": async (astro) => {
        var _a;
        (_a = astro.config.vite).plugins || (_a.plugins = []);
        astro.config.vite.plugins.push(_chunkBRLMGO66cjs.unplugin_default.vite(options));
      }
    }
  };
}


module.exports = astro_default;
exports.default = module.exports;