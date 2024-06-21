
const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});


document.addEventListener("DOMContentLoaded", function() {
    const contactUsLink = document.getElementById("contact-us");
    const contactFormPopup = document.getElementById("contact-form");
    const closeButton = document.createElement("span");
    closeButton.className = "close-button";
    closeButton.innerHTML = "&times;";
    contactFormPopup.querySelector(".container").appendChild(closeButton);
  
    contactUsLink.addEventListener("click", function(event) {
      event.preventDefault();
      contactFormPopup.style.display = "flex";
    });
  
    closeButton.addEventListener("click", function() {
      contactFormPopup.style.display = "none";
    });
  
    window.addEventListener("click", function(event) {
      if (event.target == contactFormPopup) {
        contactFormPopup.style.display = "none";
      }
    });
  });
  
