// $(document).ready(()=>{
//     const addQuantityBtn = $('.add-quantity-btn');
//     const minusQuantityBtn = $('.minus-quantity-btn');
//     let quantity = $('.quantity');
//     let total = $('.total');
//     let finalTotal = $('.final-total');
//     // ADD QUANTITY
//     addQuantityBtn.click((e)=>{
//         e.preventDefault();
//         const url = addQuantityBtn.attr('href');
//         const method = 'POST'
//         const data = {
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         }
//         $.ajax({
//             url: url,
//             method: method,
//             data: data,
//             success: (data)=>{
//                 if(url.includes(data.slug)){
//                     console.log('add included')
//                     console.log(data)
//                     quantity.text(data.quantity)
//                     total.text(`PHP ${data.total}`)
//                     finalTotal.text(`PHP ${data.finalTotal}`)
//                 }
//             },
//             error: (error)=>{
//                 console.log(error)
//             }
//         })
//     })

//     //MINUS QUANTITY
//     minusQuantityBtn.click((e)=>{
//         e.preventDefault();
//         const url = minusQuantityBtn.attr('href');
//         const method = 'POST'
//         const data = {
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         }
//         $.ajax({
//             url: url,
//             method: method,
//             data: data,
//             success: (data)=>{
//                 if(url.includes(data.slug)){
//                     console.log('minus included')
//                     console.log(data)
//                     quantity.text(data.quantity)
//                     total.text(`PHP ${data.total}`)
//                     finalTotal.text(`PHP ${data.finalTotal}`)
//                 }
                
//             },
//             error: (error)=>{
//                 console.log(error)
//             }
//         })
//     })
    
// })