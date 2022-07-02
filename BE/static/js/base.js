let display = 'block'
const showFullsize = (event, image) => {
  let element = document.getElementById(image)
  element.style.display = display
  if (display == 'block') {
    display = 'none'
  } else {
    display = 'block'
  }
}
