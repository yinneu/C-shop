var cardView = document.getElementById("modalCard");
var cardViewEffect = document.getElementById("modalEffect");

$('.stack').click(function(){
  $('#modal-container').removeAttr('class').addClass("two");
  $('body').addClass('modal-active');
  
  cardView.children[0].style.backgroundImage = $(this).children(0).css('background-image');
  

  cardView.children[1].innerHTML = $(this).children()[0].outerHTML;
    cardViewEffect.innerText = $(this).children()[1].innerText;
  
})

$('#modal-container').click(function(){
  $(this).addClass('out');
  $('body').removeClass('modal-active');
});

window.addEventListener("resize",scrollGrid);
window.addEventListener("scroll",scrollGrid);

function scrollGrid() {
	let bodyHeight = document.body.offsetHeight,
		mainHeight = document.querySelector("main").offsetHeight,
		cards = document.querySelector(".cards"),
		transY = (window.pageYOffset / (mainHeight - bodyHeight)) * -100;
	
	cards.style.setProperty("--scroll",transY + "%");
}
scrollGrid();