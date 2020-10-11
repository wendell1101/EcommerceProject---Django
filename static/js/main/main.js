
$(document).ready(()=>{
    //automatic searching
    // Auto Search
    let searchForm = $(".search-form")
    let searchInput = searchForm.find("[name='q']") // input name='q'
    let typingTimer;
    let typingInterval = 500 // .5 seconds
    let searchBtn = searchForm.find("[type='submit']")
    searchInput.keyup(function(event){
      // key released
      clearTimeout(typingTimer)

      typingTimer = setTimeout(perfomSearch, typingInterval)
    })

    searchInput.keydown(function(event){
      // key pressed
      clearTimeout(typingTimer)
    })

    function displaySearching(){
      searchBtn.addClass("disabled")
      searchBtn.html("<i class='fa fa-spin fa-spinner'></i>")
    }

    function perfomSearch(){
      displaySearching()
      let query = searchInput.val()
      setTimeout(function(){
        window.location.href='/search/?q=' + query
      }, 1000)
      
    }



    // admin deleting of product
    const btnDeleteError = $('.btn-delete-error');
    btnDeleteError.click((e)=>{
        $.alert({
            title: "Oops!",
            content: "You can't delete this product as of the moment",
            theme: "modern",
          })
    })

    //ADD OR REMOVE TO CART
    let updateCartForm = $('.cart-form');
    const removeCartBtn = $('.remove-cart-btn');
    const addCartBtn = $('.add-cart-btn');
    const cartBtn = $('.cart-btn');
    const cartItemCount = $('.cart-count');



    updateCartForm.submit((e)=>{
        e.preventDefault();
        let updateCartFormUrl = updateCartForm.attr('action');
        let updateCartFormMethod = updateCartForm.attr('method');
        let updateCartFormData= updateCartForm.serialize();
    
        $.ajax({
            url: updateCartFormUrl,
            method : updateCartFormMethod,
            data: updateCartFormData,
            success : (data)=>{   
                cartItemCount.text(data.cartItemCount)            
                if (data.added){
                    cartBtn.html(`
                        <button type='submit' class="btn btn-danger btn-md my-0 p remove-cart-btn">Remove from cart
                            <i class="fas fa-shopping-cart ml-1"></i></button>
                        </button>
                    `)
                }else if (data.removed){
                    cartBtn.html(`
                    <button type='submit' class="btn btn-primary btn-md my-0 p add-cart-btn">Add to cart
                        <i class="fas fa-shopping-cart ml-1"></i></button>
                    </button>
                    `)
                }
             
            },
            error: (error)=>{
                console.log(error)
            }
        })
        
        
    })

    //REFRESH CART COUNT

    orderProgressUrl = "{% url 'order:progress' %}";
    path = window.location.pathname;
    

   
    

 
   
})