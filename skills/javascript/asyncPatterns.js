/**
 * Async/Await Examples - Skills for GitHub Copilot CLI
 * This file demonstrates async programming patterns in JavaScript.
 */

/**
 * Simulate an async operation with a delay
 */
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Fetch data with simulated delay
 */
async function fetchData(id) {
    await delay(100);
    return { id, data: `Data for ${id}` };
}

/**
 * Fetch multiple items in parallel
 */
async function fetchMultiple(ids) {
    const promises = ids.map(id => fetchData(id));
    return await Promise.all(promises);
}

/**
 * Fetch items sequentially
 */
async function fetchSequential(ids) {
    const results = [];
    for (const id of ids) {
        const result = await fetchData(id);
        results.push(result);
    }
    return results;
}

/**
 * Retry an async operation with exponential backoff
 */
async function retryWithBackoff(fn, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
        try {
            return await fn();
        } catch (error) {
            if (i === maxRetries - 1) throw error;
            await delay(Math.pow(2, i) * 100);
        }
    }
}

/**
 * Race multiple promises and return the first to complete
 */
async function racePromises(promises) {
    return await Promise.race(promises);
}

/**
 * Execute async tasks with a timeout
 */
async function withTimeout(promise, timeoutMs) {
    const timeoutPromise = new Promise((_, reject) =>
        setTimeout(() => reject(new Error('Timeout')), timeoutMs)
    );
    return Promise.race([promise, timeoutPromise]);
}

/**
 * Process items in batches
 * Note: This processes items within each batch in parallel (using Promise.all),
 * but processes batches sequentially (using await in loop). This is useful for
 * rate limiting or when you need to control concurrent operations.
 */
async function processBatches(items, batchSize, processor) {
    const results = [];
    for (let i = 0; i < items.length; i += batchSize) {
        const batch = items.slice(i, i + batchSize);
        const batchResults = await Promise.all(batch.map(processor));
        results.push(...batchResults);
    }
    return results;
}

// Export functions
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        delay,
        fetchData,
        fetchMultiple,
        fetchSequential,
        retryWithBackoff,
        racePromises,
        withTimeout,
        processBatches
    };
}

// Test the functions if running directly
if (require.main === module) {
    (async () => {
        console.log('Testing async operations...');
        
        // Test parallel fetch
        const parallelResults = await fetchMultiple([1, 2, 3]);
        console.log('Parallel fetch:', parallelResults);
        
        // Test sequential fetch
        const sequentialResults = await fetchSequential([4, 5]);
        console.log('Sequential fetch:', sequentialResults);
        
        // Test timeout
        try {
            await withTimeout(delay(2000), 1000);
        } catch (error) {
            console.log('Timeout caught:', error.message);
        }
        
        console.log('All async tests complete!');
    })();
}
