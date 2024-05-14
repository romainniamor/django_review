function hiddenAlert() {
  const alert = document.querySelector(".alert");
  alert.classList.remove("show");
}

setTimeout(hiddenAlert, 8000);
