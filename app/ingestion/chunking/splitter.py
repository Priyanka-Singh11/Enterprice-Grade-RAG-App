from typing import List
import logfire


#this function is used to chunk the text into smaller chunks of specified size and convert into list. It splits the text by paragraphs and ensures that the chunks do not exceed the specified size. It returns a list of valid chunks.
def chunk_text(text: str, chunk_size: int = 1500) -> List[str]:
    """
    Simple semantic-ish chunker that splits by paragraphs.
    Ensures chunks do not exceed the specified size.
    """
    with logfire.span("✂️ Text Chunking", text_length=len(text)):
        if not text.strip(): 
            return []
            
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""
        
        for p in paragraphs:
            if len(current_chunk) + len(p) < chunk_size: # the length of the current chunk plus the length of the new paragraph is less than the chunk size then append it into the current chunk plus two new lines
                current_chunk += p + "\n\n"
            else:
                if current_chunk.strip():# if the current chunk is not empty then append it into the chunks list
                    chunks.append(current_chunk.strip())
                current_chunk = p + "\n\n"
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())# if the current chunk is not empty then append it into the chunks list
            
        valid_chunks = [c for c in chunks if c.strip()]
        logfire.info(f"✅ Generated {len(valid_chunks)} chunks")
        return valid_chunks