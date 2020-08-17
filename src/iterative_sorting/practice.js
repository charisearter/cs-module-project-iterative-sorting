let arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14];

function multOfThree(arr) {
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] % 3 === 0) {
			console.log(arr[i]);
		}
	}
}

multOfThree(arr);



