// DETECT ELEMENT IN VIEWPORT
let isInViewport = function (elem) {
    let bounding = elem.getBoundingClientRect();
    return (
        bounding.top >= 0 &&
        bounding.left >= 0 &&
        bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
};
// NAVIGATION HIGHLIGHTING
function navigationalHighlighting() {
    // HIGHLIGHTING LOGIC
        const navLinks = document.querySelectorAll('.nav-link');
        const mainNavLink = document.querySelector('.main-nav-link');
        mainNavLink.addEventListener('click', highlightNavMenu);
        Array.from(navLinks).forEach(element => element.addEventListener('click', highlightNavMenu));
        function addNavColorsBlack(moduleName){
            document.querySelector(`.nav-${moduleName}`).classList.add('color-black');
            document.querySelector(`.nav-link-${moduleName}`).classList.add(`give-nav-${moduleName}-background-color`);
        }
        function addNavColorsWhite(moduleName){
            document.querySelector(`.nav-${moduleName}`).classList.add('color-white');
            document.querySelector(`.nav-link-${moduleName}`).classList.add(`give-nav-${moduleName}-background-color`);
        }
        function toggleNavColorsBlack(moduleName){
            document.querySelector(`.nav-${moduleName}`).classList.toggle('color-black');
            document.querySelector(`.nav-link-${moduleName}`).classList.toggle(`give-nav-${moduleName}-background-color`);
        }
        function toggleNavColorsWhite(moduleName){
            document.querySelector(`.nav-${moduleName}`).classList.toggle('color-white');
            document.querySelector(`.nav-link-${moduleName}`).classList.toggle(`give-nav-${moduleName}-background-color`);
        }
        function resetNavColorsBlack(moduleName){
            document.querySelector(`.nav-${moduleName}`).classList.remove('color-black');
            document.querySelector(`.nav-link-${moduleName}`).classList.remove(`give-nav-${moduleName}-background-color`);
        }
        function resetNavColorsWhite(moduleName){
            document.querySelector(`.nav-${moduleName}`).classList.remove('color-black');
            document.querySelector(`.nav-link-${moduleName}`).classList.remove(`give-nav-${moduleName}-background-color`);
        }
    // HIGHLIGHT BY CLICKING ON NAV BUTTON
        function highlightNavMenu(click){
            if(click.target.classList.contains('nav-odin')){
                toggleNavColorsWhite('odin');
                resetNavColorsBlack('tyr');
                resetNavColorsWhite('mimir');
                resetNavColorsWhite('heimdall');
            }
            if(click.target.classList.contains('nav-tyr')){
                toggleNavColorsBlack('tyr');
                resetNavColorsWhite('mimir');
                resetNavColorsWhite('heimdall');
            }
            if(click.target.classList.contains('nav-mimir')){
                toggleNavColorsWhite('mimir');
                resetNavColorsBlack('tyr');
                resetNavColorsWhite('heimdall');
            }
            if(click.target.classList.contains('nav-heimdall')){
                toggleNavColorsWhite('heimdall');
                resetNavColorsBlack('tyr');
                resetNavColorsWhite('mimir');
            }
        }
    // HIGHLIGHT BY VIEWPORT DETECTION
        const functionTyr = document.getElementById('jump-tyr');
        const functionMimir = document.getElementById('jump-mimir');
        const functionHeimdall = document.getElementById('jump-heimdall');
        const functionIntro = document.getElementById('end-intro');
        window.addEventListener('scroll', function (event) {
            if (isInViewport(functionIntro)) {
                resetNavColorsBlack('tyr');
                resetNavColorsWhite('heimdall');
                resetNavColorsWhite('mimir');
                console.log('End Intro');
            }
            if (isInViewport(functionTyr)) {
                addNavColorsBlack('tyr');
                resetNavColorsWhite('mimir');
                resetNavColorsWhite('heimdall');
            }
            if (isInViewport(functionMimir)) {
                addNavColorsWhite('mimir');
                resetNavColorsBlack('tyr');
                resetNavColorsWhite('heimdall');
            }
            if (isInViewport(functionHeimdall)) {
                addNavColorsWhite('heimdall');
                resetNavColorsBlack('tyr');
                resetNavColorsWhite('mimir');
            }
        }, false);
} navigationalHighlighting();
// COLLAPSE AND EXPAND ELEMENTS
function collapseMenu() {
    const coll = document.getElementsByClassName("collapse");
    for (let i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
          content.style.display = "none";
        } else {
          content.style.display = "block";
        }
      });
    }
} collapseMenu()