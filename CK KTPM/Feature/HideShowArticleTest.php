<?php

namespace Tests\Feature;

use App\Models\Article;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;
use Tests\TestCase;

class HideShowArticleTest extends TestCase
{
    public $token = '';

    protected function setUp(): void
    {
        parent::setUp();

        $data = [
            'email' => 'benhviengiadinh@yopmail.com',
            'password' => '123456',
        ];
        $response = $this->post('api/user/login', $data);
        $responseData = $response->json();
        $this->assertArrayHasKey('access_token', $responseData['data']);
        $this->token = $responseData['data']['access_token'];
    }

    private function getAuthorizationHeaders()
    {
        return [
            'Authorization' => 'Bearer ' . $this->token,
        ];
    }

    public function testHideShowArticleSuccessful()
    {
        $article = Article::orderBy('id', 'desc')->first();
        $response = $this->post('api/article/hide-show/' . $article->id, $this->getAuthorizationHeaders());
        $response->assertStatus(200);
        $response->assertJson(['message' => 'Thay đổi trạng thái hiển thị của bài viết thành công !']);
    }

}
