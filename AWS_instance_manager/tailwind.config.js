/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
       './Instances/templates/pages/*.html',
    ],
    theme: {
      extend: {
        fontFamily: {
          'magnolia': ['Magnolia Script', 'cursive'],
        },
      },
    },
    plugins: [],
  }