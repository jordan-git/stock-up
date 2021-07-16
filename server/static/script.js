const landingBtn = document.querySelector('#landing button');
const contactBtn = document.querySelector('#contact-support button');

const emailInput = document.querySelector('#email');
const messageInput = document.querySelector('#message');

// Scroll to specified element
function scrollTo(element) {
  element.scrollIntoView({ behavior: "smooth" });
}

// Scrolls from landing to the content
landingBtn.addEventListener('click', () => {
  scrollTo(document.querySelector('.page:nth-child(2)'));
});

contactBtn.addEventListener('click', (evt) => {
  evt.preventDefault();

  contactBtn.disabled = true;
  emailInput.disabled = true;
  messageInput.disabled = true;

  alert("Your message has been submitted successfully. Expect a response within 2 working days.")

});
