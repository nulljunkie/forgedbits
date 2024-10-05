export default {
  content: [
    "./comonents/**/*.{vue,js,ts,jsx,tsx}",
    "./pages/**/*.{vue,js,ts,jsx,tsx}",
    "./layouts/*.vue",
  ],
  theme: {
    extend: {
      colors: {
        primary_red: "#f02c56",
        bg_primary: "#f5f5f5",
        blue_1: "#3b49df",
      },
    },
    fontFamily: {
      rubik: ["Rubik"],
    },

    // screens: {
    //   sm: "576px",
    //   md: "960px",
    //   lg: "1200px",
    // },
  },
  variants: {
    extend: {
      position: ["responsive", "hover", "focus"],
    },
  },
  plugins: [],
};
