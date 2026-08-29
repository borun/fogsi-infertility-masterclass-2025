/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./topics/**/*.{html,js,md}",
    "./data/**/*.json"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Plus Jakarta Sans', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      colors: {
        brand: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          500: '#0284c7',
          600: '#0369a1',
          700: '#075985',
          800: '#0c4a6e',
          900: '#082f49',
        },
        clinical: {
          teal: '#0d9488',
          emerald: '#059669',
          amber: '#d97706',
          rose: '#e11d48',
          slate: '#1e293b',
        }
      }
    },
  },
  plugins: [],
}
