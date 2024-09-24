

    let footer = document.querySelector('footer');
    let copyright = document.getElementById('copyright');
    let originalFooter = footer.innerHTML;
    let originalCopyrightStyle = String.toString(getComputedStyle(copyright));
  
    function checkFooter() {
      let currentFooter = footer.innerHTML;
      let currentCopyrightStyle = String.toString(getComputedStyle(copyright));
  
      if ((currentFooter !== originalFooter) ||
        (currentCopyrightStyle !== originalCopyrightStyle)) {
        location.href = `https://instagram.com/evolex.inc`;
      }
    }
  
    setInterval(() => {
      checkFooter()
      console.log('check');
    }, 1000);
    function es_slide1(){
        document.getElementById("page2_id1").className = "page2_id1-off";
        document.getElementById("page1_id1").className = "page1_id1"; 
       
    }
     
    function es_slide2(){ 
        document.getElementById("page1_id1").className = "page1_class1-off";
        document.getElementById("page2_id1").className = "page2_id1";
    }