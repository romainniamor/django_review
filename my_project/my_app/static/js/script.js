function hiddenAlert() {
  const alert = document.querySelector(".alert");
  alert.classList.remove("show");
}

setTimeout(hiddenAlert, 8000);

//___NAV SEARCH FORM___
document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.getElementById("search-customer-form");
  const searchInput = document.getElementById("search-customer-input");
  const searchResults = document.getElementById("search-customer-result");

  searchForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const xhr = new XMLHttpRequest();
    const formData = new FormData(searchForm);

    xhr.open("POST", searchForm.action, true);
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");

    xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          const data = JSON.parse(xhr.responseText);
          searchResults.innerHTML = "";

          if (data.error) {
            pass;
          } else if (data.message) {
            searchResults.innerHTML = `<li class="list-group-item">${data.message}</li>`;
          } else {
            data.map((customer) => {
              const listItem = document.createElement("a");
              listItem.classList.add("list-group-item");
              listItem.href = `/customer/${customer.id}`;
              listItem.textContent = `${customer.first_name} ${customer.last_name} - ${customer.city}`;
              searchResults.appendChild(listItem);
            });
          }
        } else {
          console.error("Une erreur est survenue lors de la requête AJAX");
        }
      }
    };

    xhr.send(formData);
  });
  document.addEventListener("click", function (event) {
    if (
      !searchForm.contains(event.target) &&
      !searchResults.contains(event.target)
    ) {
      searchResults.innerHTML = "";
      searchInput.value = "";
    }
  });
});
