$(document).ready(()=>{
    //ADD OR REMOVE TO CART
    let updateCartForm = $('.cart-form');
    const removeCartBtn = $('.remove-cart-btn');
    const addCartBtn = $('.add-cart-btn');
    const cartBtn = $('.cart-btn');
    const cartItemCount = $('.cart-count');



     // REFRESH CART_COUNT
    console.log(window.location.pathname)
    orderSuccessUrl = '/order/success/'
    
    const refresh_cart_count = () =>{
        $.ajax({
            url: '/order/success/',
            method : 'GET',
            data: {},
            success: (data) => {
                cartItemCount.text(data.cart_items_count)
                
            },
            error: (error) => {
                console.log('error: ',error)
            }
        })
        
    }


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

   
    

 
   
})