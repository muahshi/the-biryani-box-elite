function shareOnIG() {
    const canvas = document.getElementById('storyCanvas');
    const ctx = canvas.getContext('2d');

    // 1. Background Fill
    ctx.fillStyle = '#0a2910';
    ctx.fillRect(0, 0, 1080, 1920);

    // 2. Add Gold Border
    ctx.strokeStyle = '#c5a059';
    ctx.lineWidth = 40;
    ctx.strokeRect(50, 50, 980, 1820);

    // 3. Text Branding
    ctx.fillStyle = '#c5a059';
    ctx.font = 'bold 80px Poppins';
    ctx.fillText('THE BIRYANI BOX', 250, 250);
    
    ctx.fillStyle = '#ffffff';
    ctx.font = '50px Poppins';
    ctx.fillText('Elite Club Member Review', 250, 350);

    // 4. Placeholder for Cartoon Biryani Illustration
    ctx.fillStyle = '#c5a059';
    ctx.beginPath();
    ctx.arc(540, 900, 300, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.font = '40px Poppins';
    ctx.fillText('[ Cartoon Biryani Art ]', 400, 900);

    // 5. Download & Alert
    const image = canvas.toDataURL("image/png");
    const link = document.createElement('a');
    link.download = 'biryani-story.png';
    link.href = image;
    link.click();
    
    alert("Story Graphic Downloaded! Upload to IG, tag @TheBiryaniBox and get ₹10.");
}

