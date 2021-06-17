const landingBtn = document.querySelector('#landing button');

// Scroll to specified element
function scrollTo(element) {
  element.scrollIntoView({ behavior: "smooth" });
}

// Scrolls from landing to the content
landingBtn.addEventListener('click', () => {
  scrollTo(document.querySelector('section:nth-child(2)'));
});