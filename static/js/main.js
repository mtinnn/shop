function totalitem(click) {
    const totalitems = document.getElementById('total-item');
    const sumvalue = parseInt(totalitems.innerText) + click;

    totalitems.innerText = sumvalue

}