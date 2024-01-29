/** @type {import('tailwindcss').Config}*/
const config = {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  theme: {
    extend: {}
  },

  plugins: [require('daisyui')],

  daisyui: {
    themes: [
      {
        corporate: {
          ...require('daisyui/src/theming/themes')['[data-theme=corporate]'],
          primary: '#7ab187',
          secondary: '#61ba76'
        }
      }
    ]
  }
};

module.exports = config;
