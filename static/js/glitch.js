
var canvas = document.getElementById('Goran')
  , context = canvas.getContext('2d')
  , img = new Image()
  , w
  , h
  , offset
  , glitchInterval;

img.src = '/static/img/Picture 1.jpg';
img.onload = function() {
  init();
	window.onresize = init;
};

var init = function() {
	clearInterval(glitchInterval);
	canvas.width = w = window.innerWidth / 3;
	console.log(w)
	// canvas.width = w = 650
	offset = w * .1;
	canvas.height = h = ~~(400 * ((w - (offset * 2)) / img.width));
	glitchInterval = setInterval(function() {
		clear();
		context.drawImage(img, 0, 70, img.width,
                      400, offset, 0, w - (offset * 2), h);
		setTimeout(glitchImg, randInt(250, 1000));
	}, 500);
};

var clear = function() {
	context.rect(0, 0, w, h);
	context.fillStyle = '#18BC9C';
	context.fill();
};

var glitchImg = function() {
	for (var i = 0; i < randInt(1, 13); i++) {
		var x = Math.random() * w;
		var y = Math.random() * h;
		var spliceWidth = w - x;
		var spliceHeight = randInt(5, h / 3);
		context.drawImage(canvas, 0, y, spliceWidth, spliceHeight, x, y, spliceWidth, spliceHeight);
		context.drawImage(canvas, spliceWidth, y, x, spliceHeight, 0, y, x, spliceHeight);
	}
};

var randInt = function(a, b) {
	return ~~(Math.random() * (b - a) + a);
};
