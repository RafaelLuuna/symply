const navBar = document.querySelector('#nav-links');
function toggleNavBar(){
    if(window.innerWidth > 768){
        navBar.classList.add('show');
    }
    else{
        navBar.classList.remove('show');

    }
}
window.onresize = toggleNavBar;
window.onload = toggleNavBar;

scrollLimit = 350;
window.onscroll = ()=>{
    console.log(window.scrollY);
    const element = document.getElementById('header');
    const baseCalss = 'header-container';
    if(window.scrollY > scrollLimit)
    {
        header.className = `${baseCalss} outview`;
    }
    else
    {
        if(window.scrollY > element.getBoundingClientRect().height){
            if(header.className == `${baseCalss} outview`){
                header.className = `${baseCalss} quiting`;
            }
        }
        else{
            header.className = `${baseCalss}`;
        }
    }
};


const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
        const childElements = entry.target.children;
        for (const element of childElements){
            const computedStyle = window.getComputedStyle(element);
            if(computedStyle.animationName !== 'none'){
                const animation = computedStyle.animationName;
                
                element.style.animationName  = 'none';
                void element.offsetWidth;
                element.style.animationName  = animation;
            }
        };

    }
  });
}, {
  rootMargin: '40px'
});

const widgetList = document.querySelectorAll('*[class*="widget"]');
widgetList.forEach( widget =>{
    observer.observe(widget);
});

