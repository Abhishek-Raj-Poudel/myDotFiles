/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './views/**/*.{html,ejs}',
    './node_modules/tw-elements/dist/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#dcad25',
        pastelBlack: '#1D1C1A',
      },
      fontFamily: {
        primary: 'Avenir',
        secondary: ['Nunito', 'sans-serif'],
      },
      animation: {
        textSwipeUp: 'textSwipeUp 10s infinite',
        whiteOut: 'whiteOut 5s infinite',
        marquee: 'marquee 25s linear infinite',
        marquee2: 'marquee2 25s linear infinite',
        reverseMarquee: 'reverseMarquee 25s linear infinite',
        reverseMarquee2: 'reverseMarquee2 25s linear infinite',
      },
      keyframes: {
        textSwipeUp: {
          '0%': { opacity: '0', transform: 'translateY(-40%)' },
          '10%': { opacity: '1', transform: 'translateY(-50%)' },
          '15%': { opacity: '1', transform: 'translateY(-50%)' },
          '20%': { opacity: '0', transform: 'translateY(-60%)' },
          '100%': { opacity: '0', transform: 'translateY(-60%)' },
        },
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-100%)' },
        },
        marquee2: {
          '0%': { transform: 'translateX(100%)' },
          '100%': { transform: 'translateX(0%)' },
        },
        reverseMarquee: {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(0%)' },
        },
        marquee2: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(100%)' },
        },
      },
    },
  },
  plugins: [require('tw-elements/dist/plugin.cjs'), require('autoprefixer')],
};
