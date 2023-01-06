const request = new XMLHttpRequest();
request.open('GET', 'https://mushytoast.github.io');
request.onload = () => {
    console.log(request.responseText);
};