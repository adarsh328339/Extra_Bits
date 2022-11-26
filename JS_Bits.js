// Finding the union and intersection of two arrays using JavaScript 

arr1 = [1,2,3,4,5,6]
arr2 = [3,4,5,7]

const arr_intersect = arr1.filter((ele) => {
    return arr2.includes(ele)
})
console.log('This is the intersection of the array:-', arr_intersect)

const arr_union = [...new Set([...arr1, ...arr2])]

console.log('This is the union of the arrays:-', arr_union)

    
