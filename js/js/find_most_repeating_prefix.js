function findMostRepeatingPrefix(words){
    let currentPrefix = words[0];
    let longestPrefix = currentPrefix;
    let longestPrefixCount = 1;
    
    let inlineItemCount = 1;
    for( let i = 1 ; i < arr.length  ; i++ ){
        const str = arr[i];
        let currentPrefixCount = 0;
        for( let j = 0 ; j < str.length ; j++ ){
            if( str[j] == currentPrefix[j] ){
                currentPrefixCount++;
            }
            else break;
        }
        
        if( currentPrefixCount > 0 ) {
            inlineItemCount++;
            if( currentPrefixCount < currentPrefix.length ){
                currentPrefix = currentPrefix.slice(0 , currentPrefixCount);
            }
        }
        
        else {
            if( inlineItemCount >= longestPrefixCount ){
                longestPrefixCount = inlineItemCount;
                longestPrefix = currentPrefix;
                inlineItemCount = 0;
            }
            
            currentPrefix = str;
        }
    }
    
    return longestPrefix;
}

const arr = ['asd1','asd12','fdfdf','dddsd','789kley','8789kl','789kuu','asd'];

console.log(findMostRepeatingPrefix(arr));