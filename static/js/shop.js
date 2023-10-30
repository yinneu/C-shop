var cardView = document.getElementById("modalCard");
var cardViewEffect = document.getElementById("modalEffect");
var cardViewPrice = document.getElementById("price"); //금액


$('.stack').click(function(){
  $('#modal-container').removeAttr('class').addClass("two");
  $('body').addClass('modal-active');
  
  cardView.children[0].style.backgroundImage = $(this).children(0).css('background-image');
  
  cardView.children[1].innerHTML = $(this).children()[0].outerHTML;
    cardViewEffect.innerText = $(this).children()[1].innerText;
    cardViewPrice.innerText = 'x ' + $(this).children()[2].innerText;
  
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


//추가할 사항
//구매 버튼 클릭시 로그인한 상태가 아니면 로그인
//로그인 상태면 유저의 열매개수와 해당 구매권을 비교하고 구매가 불가능을 알려줌. (check를 날리기)
//구매요청을 날리면 백에서 구매 여부 확인후 불가능이면 false, 가능이면 구매할것인지 확인 후