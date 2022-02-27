// NAVIGATION HIGHLIGHTING
const navLinks = document.querySelectorAll('.nav-link');
const mainNavLink = document.querySelector('.main-nav-link');
mainNavLink.addEventListener('click', highlightNavMenu);
Array.from(navLinks).forEach(element => element.addEventListener('click', highlightNavMenu));
function giveNavColorsBlack(moduleName){
    document.querySelector(`.nav-${moduleName}`).classList.toggle('color-black');
    document.querySelector(`.nav-link-${moduleName}`).classList.toggle(`give-nav-${moduleName}-background-color`);
}
function giveNavColorsWhite(moduleName){
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
function highlightNavMenu(click){
    if(click.target.classList.contains('nav-odin')){
        giveNavColorsWhite('odin');
        resetNavColorsBlack('tyr');
        resetNavColorsWhite('mimir');
        resetNavColorsWhite('heimdall');
    }
    if(click.target.classList.contains('nav-tyr')){
        giveNavColorsBlack('tyr');
        resetNavColorsWhite('mimir');
        resetNavColorsWhite('heimdall');
    }
    if(click.target.classList.contains('nav-mimir')){
        giveNavColorsWhite('mimir');
        resetNavColorsBlack('tyr');
        resetNavColorsWhite('heimdall');
    }
    if(click.target.classList.contains('nav-heimdall')){
        giveNavColorsWhite('heimdall');
        resetNavColorsBlack('tyr');
        resetNavColorsWhite('mimir');
    }
}

