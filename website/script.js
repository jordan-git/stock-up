const landingBtn = document.querySelector('#landing button');

function scrollTo(element) {
  element.scrollIntoView({ behavior: "smooth" });
}

landingBtn.addEventListener('click', () => scrollTo(document.querySelector('section:nth-child(2)')));