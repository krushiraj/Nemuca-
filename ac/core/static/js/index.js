var svg = document.getElementById('menu'),
    itemContainer = document.getElementById('itemsContainer'),
    items = svg.querySelectorAll('.item'),
    itemsectors = document.querySelectorAll('.sector'),
    trigger = document.getElementById('trigger'),
    label = trigger.querySelectorAll('#label')[0],
    open = true,
    angle = 45,
    outer = document.getElementById("outer"),
    inner = document.getElementById("inner"),
    defMatrix = itemContainer.getAttribute("transform"),
    anim = document.getElementById('ani-svg'),
    svgbox = document.getElementById("svgbox"),
    butl = document.getElementById("rotButtonl"),
    butr = document.getElementById("rotButtonr"),
    scrollLogo = document.getElementById("sd-indicator0"),
    scrollNav = document.getElementsByClassName("sd-indicator1"),
    scrollToNav = document.getElementsByClassName("sd-indicator2"),
    body = document.body;
var lastLabel,
    logoScrolled = false,
    navScrolled = false,
    restrictScroll = true;

    
if((window.location.hash!="#nav")||(window.location.hash==="")) {
    closeNav();
}
if(open)
{
    outer.style.filter = "url(#glow)";
}
  
function jumpEffect(e) {
    if(!logoScrolled){
        $('html, body').animate({
            scrollTop: window.innerHeight*0.1
        }, 150);
        $('html, body').animate({
            scrollTop: 0
        }, 100);
        $('html, body').animate({
            scrollTop: window.innerHeight*0.05
        }, 80);
        $('html, body').animate({
            scrollTop: 0
        }, 80);
    }
}

for(var i=0;i<8;i++)
{
    items[i].addEventListener("mouseover", changeText, false);
    items[i].addEventListener("mouseout", function(e){
        label.innerHTML = lastLabel;
    }, false);
}

function changeText(e){
    var itemid = this.id;
    lastLabel = label.innerHTML;
    switch(itemid[5])
    {
        case '1':label.innerHTML = "Home";break; 
        case '2':label.innerHTML = "Sponsors";break; 
        case '3':label.innerHTML = "Registration";break; 
        case '4':label.innerHTML = "Events";break; 
        case '5':label.innerHTML = "Map";break; 
        case '6':label.innerHTML = "Team";break; 
        case '7':label.innerHTML = "Social";break; 
        case '8':label.innerHTML = "Gallery";break; 
    }
}


function getMyChildren(node)
{
    var childList = node.children;
    var arr = new Array(2);
    for(var i in childList)
    {
        if(childList[i].nodeName == "circle")
        {
            arr[0] = childList[i];
        }
        if(childList[i].nodeName == "use")
        {
            arr[1] = childList[i];
        }
        if(arr[0] && arr[1])
        {
            return arr;
        }
    }
}

function setPositions(items)
{
    var len = items.length;
    for(var i = 0; i < len; i++)
    {
        var childArr = getMyChildren(items[i]);
        var cir = childArr[0];
        var icon = childArr[1];
        var cen = icon.getBBox();
        //dont ask me why its +4. If its working then dont touch it #ruleNo-2
        cir.cx.baseVal.value = Math.ceil(cen.x + (cen.width/2)) + 4 ;
        cir.cy.baseVal.value = Math.ceil(cen.y + (cen.height/2));
        cir.style.opacity = "1";
        var innerhtml = items[i].innerHTML;
        items[i].innerHTML = '<line x1="'+cir.cx.baseVal.value+'" y1="'+cir.cy.baseVal.value+'" x2="250" y2="250" style="stroke:cyan;stroke-width:2;pointer-events:none" style="filter:url(#glow)"/>'.concat(innerhtml);
    }
}

var pointerdown = false,
    pointermove = false,
    toggleClicked = false,
    x1,x2,y1,y2;

setPositions(items);
//set up event handler
trigger.addEventListener('click', toggleMenu, false);
// svg.style.pointerEvents = "none";

butl.addEventListener('click', function(e) {
    e.stopPropagation();
    rotateSVG(-45);
}, false);
butr.addEventListener('click', function(e) {
    e.stopPropagation();
    rotateSVG(45);
}, false);

svg.addEventListener("pointerdown", pointDown, false);
svg.addEventListener("touchstart", touchDown, false);
//svg.addEventListener("mousedown", pointDown, false);

function pointDown(e) {
    if(open) {    
        x1 = e.screenX;
        y1 = e.screenY;
    }
}

function touchDown(e) {
    console.log("start"+e.target.classList);
    if(open) {    
        x1 = e.changedTouches[0].screenX;
        y1 = e.changedTouches[0].screenY;
    }

}

svg.addEventListener("touchmove",function(e) { e.preventDefault()}, false);
svg.addEventListener("mousemove",function(e) { e.preventDefault()}, false);
//svgbox.addEventListener("pointermove",function(e) { e.preventDefault()}, false);

//svgbox.addEventListener("pointerup", pointUp, false);
svg.addEventListener("touchend", touchUp, false);
svg.addEventListener("mouseup", pointUp, false);

function setNavText()
{
    var currAngle = (parseInt((anim.getAttribute("to")))%360)/45;
    currAngle = currAngle >= 0 ? currAngle : 8+currAngle;
    switch(currAngle)
    {
        case 0: label.innerHTML = "Home"; break;
        case 1: label.innerHTML = "Sponsors"; break;
        case 2: label.innerHTML = "Registration"; break;
        case 3: label.innerHTML = "Events"; break;
        case 4: label.innerHTML = "Map"; break;
        case 5: label.innerHTML = "Team"; break;
        case 6: label.innerHTML = "Social"; break;
        case 7: label.innerHTML = "Gallery"; break;
    }
}

function diff(a,b)
{
    if(a>b)
        return a-b;
    else
        return b-a;
}

function pointUp(e) {
    if(open) { 
        x2 = e.screenX;
        y2 = e.screenY;
        var diffy = diff(y1,y2);
        var diffx = diff(x1,x2);
        if(diffx <= 50 && diffy <= 50)
        {
            return;
        }
        var dir = diffx>diffy ? (x1<x2 ? 0 : 1) : (y1<y2 ? 1 : 0);
        if(dir) 
        {
             rotateSVG(45);
            //setNavText();
        }
        else
        {
            rotateSVG(-45);
        }
    }
}

function touchUp(e) {
    console.log("End"+e.target.classList);
    if(open) { 
        x2 = e.changedTouches[0].screenX;
        y2 = e.changedTouches[0].screenY;
        var diffy = diff(y1,y2);
        var diffx = diff(x1,x2);
        if(diffx <= 50 && diffy <= 50)
        {
            return;
        }
        var dir = diffx>diffy ? (x1<x2 ? 0 : 1) : (y1<y2 ? 1 : 0);
        if(dir) 
        {
             rotateSVG(45);
            //setNavText();
        }
        else
        {
            rotateSVG(-45);
        }
    }
}


function closeNav()
{
    open=false;
    var tl = new TimelineLite();
    for(var i=0; i<items.length; i++){
      tl.to(items[i], 0.3, {rotation: 0, ease:Circ.easeOut}, 0.05);
    }
    
    tl.to(items, .3, {scale:0, ease:Back.easeIn}, 0.3);
    label.innerHTML = "Home";
    svg.style.pointerEvents = "none";
    outer.r.baseVal.value -= 30;
    inner.r.baseVal.value -= 30;
    label.style.fontSize = "1em";
    rotateSVG(0);
}


function openNav() {
    var tl = new TimelineLite();
  	tl.to(items, 0.2, {scale:1, ease:Back.easeOut.config(4)}, 0.05);
    
    for(var i=0; i<items.length; i++){
      tl.to(items[i], 0.7, {rotation:-i*angle + "deg", ease:Bounce.easeOut}, 0.35);
    }
    outer.r.baseVal.value += 30;
    inner.r.baseVal.value += 30;
    label.style.fontSize = "1.5em"
    label.innerHTML = "Home";
    svg.style.pointerEvents = "auto";
}

//toggle menu when trigger is clicked
function toggleMenu(event) {
   if (!event){ var event = window.event;
    event.stopPropagation();
    }
  open = !open;
  if (open) {
    var tl = new TimelineLite();
  	tl.to(items, 0.2, {scale:1, ease:Back.easeOut.config(1)}, 0.05);
    
    for(var i=0; i<items.length; i++){
      tl.to(items[i], 0.7, {rotation:-i*angle + "deg", ease:Bounce.easeOut}, 0.35);
    }
    outer.r.baseVal.value += 30;
    inner.r.baseVal.value += 30;
    label.style.fontSize = "1.5em"
    label.innerHTML = "Home";
    svg.style.pointerEvents = "auto";
    outer.style.filter = "url(#glow)";
  } 
  else {
        setNavText();
        switch(label.innerHTML)
        {
            case 'Home': closeNav();outer.style.filter = "none"; return; 
            case 'Sponsors': window.location.href = "{% url 'sponsors' %}";return;
            case 'Registration': window.location.href = "{% url 'signup' %}";return;
            case 'Events': window.location.href = "{% url 'events' %}";return;
            case 'Map': window.location.href = "{% url 'maps' %}";return;
            case 'Team': window.location.href = "{% url 'team' %}";return;
            case 'Social': window.location.href = "{% url 'social' %}";return;
            case 'Gallery': window.location.href = "{% url 'gallery' %}";return;
        }
  }
  
}

svg.onclick = function (e) {
    e.stopPropagation();
}
//close the nav when document is clicked
document.onclick = function () {
    if(open)
    {
        open = false;
        var tl = new TimelineLite();
        for(var i=0; i<items.length; i++){
          tl.to(items[i], 0.3, {rotation: 0, ease:Circ.easeOut}, 0.05);
        }
        tl.to(items, .3, {scale:0, ease:Back.easeIn}, 0.3);
        label.innerHTML = "Home";
        svg.style.pointerEvents = "none";
        outer.r.baseVal.value -= 30;
        inner.r.baseVal.value -= 30;
        label.style.fontSize = "1em";
        outer.style.filter = "none";
        resetRotation();
    }
};

//rotate matrix of group
function rotateSVG(deg)
{   
    if(open){
        var prevAngle = parseInt(anim.getAttribute("to"));
        anim.setAttribute("from",prevAngle.toString());
        anim.setAttribute("to",((prevAngle+deg)).toString());
        anim.beginElement();
        var prevLabel = parseInt((label.getAttribute("transform")).split("(")[1].split(",")[0]);
        label.setAttribute("transform","rotate("+((prevLabel-deg))+",250,250)");
        setNavText();
    }
}

function resetRotation()
{
    var prevAngle = parseInt(anim.getAttribute("to"));
    anim.setAttribute("from",prevAngle.toString());
    anim.setAttribute("to","0");
    anim.beginElement();
    label.setAttribute("transform","rotate(0,250,250)");
}

