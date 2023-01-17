var count = 0
const randomwords = ['Hello', 'World', 'How', 'Are', 'You', 'Today', 'I', 'Am', 'Fine', 'Thank', 'You', 'Nice', 'To', 'Meet', 'You', 'Good', 'Bye', 'See', 'You', 'Tomorrow']
function hw() {
  count += 1
  console.log(randomwords)
}

setInterval(hw, 2)