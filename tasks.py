from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research Task
research_task = Task(
    description=(
        "Identify the video on the topic {topic}. "
        "Get detailed information about the video from the channel video."
    ),
    expected_output='A comprehensive 3-paragraph report based on the video content related to the {topic}.',
    tools=[yt_tool],
    agent=blog_researcher,
)

# Writing Task
write_task = Task(
    description=(
        "Get the information from the YouTube channel on the topic {topic}. "
        "Summarize this information and create content for the blog."
    ),
    expected_output='Summarize the information from the YouTube channel video on the topic {topic} and create content for the blog.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'  # Example of output customization
)
