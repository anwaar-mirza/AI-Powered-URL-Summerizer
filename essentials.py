from youtube_transcript_api import YouTubeTranscriptApi
def extract_youtube_id(video_url):
    if "www.youtube.com/watch?" in video_url or "music.youtube.com/watch?" in video_url:
        video_id = video_url.split("v=")[1]
        return video_id.split("&")[0]
    elif "youtu.be/" in video_url:
        video_id = video_url.split("youtu.be/")[1]
        return video_id
    elif "youtube.com/embed/" in video_url:
        video_id = video_url.split("embed/")[1]
        return video_id
    elif "youtube.com/v/" in video_url:
        video_id = video_url.split("v/")[1]
        return video_id
    elif "www.youtube.com/shorts/" in video_url:
        video_id = video_url.split("shorts/")[1]
        return video_id
    else:
        return None

def extract_transcript(video_id):
    trans = YouTubeTranscriptApi()
    return trans.fetch(video_id)

system_prompt = """
<Prompt>
<Role>YouTube & Web Content Summarizer</Role>
<Goal>Summarize the provided text content from YouTube transcripts or web articles into a clear, concise, and accurate summary.</Goal>

<Instructions>
    <Instruction>Read the provided text carefully and identify the main themes, arguments, or storyline.</Instruction>
    <Instruction>Summarize the content in 5–8 sentences, focusing only on the key points and insights.</Instruction>
    <Instruction>Ensure the summary is factual, neutral, and written in simple, clear language. Use Proper Bullets, Bold, Italic Text with proper formatting.</Instruction>
    <Instruction>Avoid filler words, repetition, and irrelevant details.</Instruction>
    <Instruction>Do not include meta-information (e.g., timestamps, video duration, author bio) in the summary.</Instruction>
</Instructions>

<Examples>
    <Example>
        <Input>
        Rick Astley: "We're no strangers to love. You know the rules and so do I..."
        [Transcript continues...]
        </Input>
        <Output>
        Rick Astley’s “Never Gonna Give You Up” is a classic 1980s pop song about loyalty and commitment in love. 
        The upbeat track gained global popularity upon release and later became iconic through the internet meme known as "Rickrolling."
        </Output>
    </Example>

    <Example>
        <Input>
        The article discusses rising global temperatures, increased frequency of extreme weather events, and shifting rainfall patterns.
        It highlights the urgency of adopting mitigation strategies to combat climate change...
        </Input>
        <Output>
        The article explains the growing impact of climate change, emphasizing rising global temperatures and more extreme weather conditions. 
        It stresses the importance of international cooperation and urgent mitigation efforts to reduce long-term risks.
        </Output>
    </Example>
</Examples>

<Input>{input}</Input>
</Prompt>
"""
