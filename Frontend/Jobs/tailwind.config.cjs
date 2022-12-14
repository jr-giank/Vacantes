/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx}"],
  theme: {
    extend: {},

    colors: {
      primary: '#1B3351',
      black: '#000',
      secondary: '#23C647',
      tertiary: '#E6E8E6',
      fourth: '#DF2935',
      fifth: '#E6E8E6',
      sixth: '#C0C0C0',
      seventh: '#0A66CE',
      eighth: '#f4f4f5',
      nineth: '#e0f2fe',
      tenth: 'rgba(0, 0, 0, 0.71)',
      eleventh: '#F5F5F5',
      twelve: '#2d3954',
      thirteen: '#CDE9FE',
      white : '#fff',
      dark: '#141414',
      dark2: '#1F1F1F'
    },

    fontFamily: {
      inter :   ['Inter', 'sans-serif'],
      poppins : ['Poppins', 'sans-serif']
    }
  },
  plugins: [],
}