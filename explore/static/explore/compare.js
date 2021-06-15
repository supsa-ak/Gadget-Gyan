console.log('working');
if (localStorage.getItem('compare') == null) {
    var compare = {};
}
else {
    compare = JSON.parse(localStorage.getItem('compare'));
}
$('.compare').click(function () {
    console.log('clicked');
    var idstr = this.id.toString();
    console.log(idstr);
    if (compare[idstr] != undefined) {
        compare[idstr] = compare[idstr] + 1;
    }
    else {
        compare[idstr] = 1;
    }
    console.log(compare);
    localStorage.setItem('compare', JSON.stringify(compare));
    document.getElementById('compare').innerHTML = Object.keys(compare).length;
});

