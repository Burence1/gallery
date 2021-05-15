function copy() {
  $("#copy-url").select()
  document.execCommand('copy');
  alert("Share link has been copied to your clipboard!")
}