<?php

namespace Tests\Feature;

use Tests\TestCase;

class UserLoginTest extends TestCase
{
    public function testUserLoginLackEmail()
    {
        $data = [
            'email' => '',
            'password' => '123456',
        ];
        $response = $this->post('api/user/login', $data);
        $response->assertStatus(400);
        $response->assertJson(['message' => 'Email không tồn tại !']);
    }

    public function testUserLoginLackPassword()
    {
        $data = [
            'email' => 'benhviengiadinh@yopmail.com',
            'password' => '',
        ];
        $response = $this->post('api/user/login', $data);
        $response->assertStatus(400);
        $response->assertJson(['message' => 'Email hoặc mật khẩu không chính xác !']);
    }

    public function testUserLoginSuccessful()
    {
        $data = [
            'email' => 'benhviengiadinh@yopmail.com',
            'password' => '123456',
        ];
        $response = $this->post('api/user/login', $data);
        $response->assertStatus(200);
        $response->assertJson(['message' => 'Đăng nhập thành công !']);
    }
}
