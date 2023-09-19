gsap.registerPlugin(ScrollTrigger);
const brandingButton = document.getElementById('brandingButton');
const technologyButton = document.getElementById('technologyButton');
const brandingContent = document.getElementById('brandingContent');
const technologyContent = document.getElementById('technologyContent');

function turnOnBrandingService() {
  brandingButton.classList.add('button-active');
  brandingButton.classList.remove('button-inactive');
  technologyButton.classList.remove('button-active');
  technologyButton.classList.add('button-inactive');
  brandingContent.classList.remove('hidden');
  technologyContent.classList.add('hidden');
}
function turnOnTechnlogyService() {
  technologyButton.classList.add('button-active');
  technologyButton.classList.remove('button-inactive');
  brandingButton.classList.remove('button-active');
  brandingButton.classList.add('button-inactive');
  technologyContent.classList.remove('hidden');
  brandingContent.classList.add('hidden');
}

let animationDuration = .25;
let staggerDuration= .20;

// Hero Section Fade Up animation.
gsap.fromTo(
  '.heroSectonFadeUp',
  { x: -100, opacity: 0 },
  {
    scrollTrigger: {
      trigger: '.heroSectonFadeUp',
      start: '60% bottom 50% 0%',
      // markers: true,
    },
    x: 0,
    opacity: 1,
    duration: animationDuration,
    stagger: staggerDuration,
  },
);
// workCard Section Fade Up animation.
gsap.fromTo(
  '.workCard',
  { y: 100, opacity: 0 },
  {
    scrollTrigger: {
      trigger: '.workCard',
      start: '30% bottom 50% 0%',
      // markers: true,
    },
    y: 0,
    opacity: 1,
    duration: animationDuration,
    stagger: staggerDuration,
  },
);
// Blog Section Fade Up animation.
gsap.fromTo(
  '.blogSectonFadeUp',
  { y: 100, opacity: 0 },
  {
    scrollTrigger: {
      trigger: '.blogSectonFadeUp',
      start: '60% bottom 50% 0%',
      // markers: true,
    },
    y: 0,
    opacity: 1,
    duration: animationDuration,
    stagger: staggerDuration,
  },
);
// Event Section Fade Up animation.
gsap.fromTo(
  '.EventSectonFadeUp',
  { y: 100, opacity: 0 },
  {
    scrollTrigger: {
      trigger: '.EventSectonFadeUp',
      start: '60% bottom 50% 0%',
      // markers: true,
    },
    y: 0,
    opacity: 1,
    duration: animationDuration,
    stagger: staggerDuration,
  },
);
