/*const sidebarToggle = document.querySelector("#sidebar-toggle");
sidebarToggle.addEventListener("click", function () {
    document.querySelector("#sidebar").classList.toggle("collapsed");
});

document.querySelector(".theme-toggle").addEventListener("click", () => {
    toggleLocalStorage();
    toggleRootClass();
});

function toggleRootClass() {
    const current = document.documentElement.getAttribute('data-bs-theme');
    const inverted = current == 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-bs-theme', inverted);
}

function toggleLocalStorage() {
    if (isLight()) {
        localStorage.removeItem("light");
    } else {
        localStorage.setItem("light", "set");
    }
}

function isLight() {
    return localStorage.getItem("light");
}

if (isLight()) {
    toggleRootClass();
} */

    let footer = document.querySelector('footer');
    let copyright = document.getElementById('copyright');
    let originalFooter = footer.innerHTML;
    let originalCopyrightStyle = String.toString(getComputedStyle(copyright));
  
    function checkFooter() {
      let currentFooter = footer.innerHTML;
      let currentCopyrightStyle = String.toString(getComputedStyle(copyright));
  
      if ((currentFooter !== originalFooter) ||
        (currentCopyrightStyle !== originalCopyrightStyle)) {
        location.href = `https://instagram.com/evolex.inc`;
      }
    }
  
    setInterval(() => {
      checkFooter()
      console.log('check');
    }, 1000);