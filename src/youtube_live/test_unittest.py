from youtube_live.utils import get_youtube_video_id


class TestYoutubeLiveUtils:

    def test_get_youtube_video_id(self):

        test_obj = "https://www.youtube.com/watch?v=jfKfPfyJRdk"
        result_obj = "jfKfPfyJRdk"
        the_result = bool(result_obj == get_youtube_video_id(test_obj))
        error_message = (
            "Failed to extract video id from watch URL query string"
        )
        assert the_result, error_message

        test_obj = "https://www.youtube.com/live/jfKfPfyJRdk"
        result_obj = "jfKfPfyJRdk"
        the_result = bool(result_obj == get_youtube_video_id(test_obj))
        error_message = "Failed to extract video id from live URL"
        assert the_result, error_message

        test_obj = "jfKfPfyJRdk"
        result_obj = "jfKfPfyJRdk"
        the_result = bool(result_obj == get_youtube_video_id(test_obj))
        error_message = "Failed to extract video id from video id string"
        assert the_result, error_message

        test_obj = "jfKfPfyJRdka"
        result_obj = ""
        the_result = bool(result_obj == get_youtube_video_id(test_obj))
        error_message = "Failed to extract video id from fake video id string"
        assert the_result, error_message
