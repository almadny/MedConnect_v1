export const getPublishedArticles = async () => {
  try {
    const response = await fetch('/api/blog/posts');
    if (!response.ok) {
      throw new Error(`Failed to fetch articles (${response.status})`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching articles: ", error);
    throw error;
  }
};

export const publishArticle = async (articleData) => {
  try {
    const response = await fetch('api/blog/addpost', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(articleData),
    });
    if (!response.ok) {
      throw new Error(`Failed to publish article (${response.status})`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error publishing article: ", error);
    throw error;
  }
};

export const saveArticle = async (articleData) => {
  try {
    const response = await fetch(`/articles`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(articleData),
    });
    if (!response.ok) {
      throw new Error(`Failed to save article (${response.status})`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error saving article: ", error);
    throw error;
  }
};