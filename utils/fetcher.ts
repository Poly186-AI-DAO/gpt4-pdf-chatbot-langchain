export async function fetcher(url: string, body: any) {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
  
    if (!res.ok) {
      throw new Error('Network response was not ok.');
    }
  
    return res.json();
  }