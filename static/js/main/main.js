
$(document).ready(()=>{

    //ADD OR REMOVE TO CART
    const btnDeleteError = $('.btn-delete-error');
    btnDeleteError.click((e)=>{
        $.alert({
            title: "Oops!",
            content: "You can't delete this product as of the moment",
            theme: "modern",
          })
    })


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