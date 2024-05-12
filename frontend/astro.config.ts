import { defineConfig } from "astro/config"

// Astro integration imports
import tailwind from "@astrojs/tailwind"
import sitemap from "@astrojs/sitemap"
import compress from "astro-compress"
import { VitePWA } from "vite-plugin-pwa"
// import react from "@astrojs/react"

// Helper imports
import { manifest, seoConfig } from "./utils/seoConfig"
import type { AstroIntegration } from "astro"
import react from "@astrojs/react"

// https://astro.build/config
export default defineConfig({
	// base: '/static/', // Only when deploying
	site: seoConfig.baseURL,
	// output: "static",
	integrations: [
		tailwind({
			applyBaseStyles: false,
			configFile: "./tailwind.config.js"
		}),
		sitemap(),
		(await import("astro-compress")).default() as AstroIntegration,
		react()
	],
	vite: {
		// appType: "spa",
		plugins: [
			VitePWA({
				registerType: "autoUpdate",
				manifest,
				workbox: {
					globDirectory: "dist",
					globPatterns: [
						"**/*.{js,css,svg,png,jpg,jpeg,gif,webp,woff,woff2,ttf,eot,ico}"
					],
					// Don't fallback on document based (e.g. `/some-page`) requests
					// This removes an errant console.log message from showing up.
					navigateFallback: null
				}
			})
		]
	}
})
