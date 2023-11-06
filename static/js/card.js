// 카드 애니메이션
const cards = document.querySelectorAll('.card');
function transition() {
  if (this.classList.contains('card-active')) {
    this.classList.remove('card-active')
  } else {
    this.classList.add('card-active');
  }
}
cards.forEach(card => card.addEventListener('click', transition));
